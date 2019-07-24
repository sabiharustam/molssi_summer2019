import numpy as np


def generate_initial_state(method, box_length=None, n_particles=None, file_name=None):
    """
    This function generates initial coordinates of a LJ fluid simulation  either randomly or from a file.

    Parameters
    ----------

    method : str
        What method to use when generating initial configurations. options are 'random' or 'file'
    box_length : float/int
        length of simulation box. This is only required if the method is 'random'
    n_particles : int
        number of particles in the simulation box. This is only required if the method is 'random'
    file_name : str
        string of file to load into the simulation box. This is only required if the method is 'file'

    Returns
    -------
    coordinates in numpy array format.
    """
    
    # 2 methods:
    # 1 random initial config
    # 2 get state from NIST
    
    coordinates = None
    
    if method is 'random':
        # generate coordinates randomly in box volume
        
        coordinates = box_length*(0.5 - np.random.rand(n_particles, 3))

    elif method is 'file':
        coordinates = np.loadtxt(file_name, skiprows=2, usecols=(1, 2, 3))

    return coordinates


def LJ_potential(rij2):
    """
    returns the LJ energy for a given rij distance
    
    Parameters
    ----------

    rij2 : float
        square of distance rij between two particles

    Returns
    -------
    
    energy : float
        LJ potential energy
    """
    
    energy = 4*(np.power(1/rij2, 6) - np.power(1/rij2, 3))
    return energy


def LJ_cutoff_correction(box_length, rij_cutoff, N):
    """
    returns the LJ energy cutoff correction
    """
    V = box_length**3
    correction = 8 * np.pi * np.power(N,2) / ( 3 * V ) * ( (1 / 3) * np.power(1/rij_cutoff, 9) - np.power(1/rij_cutoff, 3))

    return(correction)


def minimum_image_distance(r_i, r_j, box_length):
    """
    returns the minimum image distance between two particles
    """

    rij = r_i - r_j
    rij = rij - box_length * np.round(rij / box_length)
    rij2 = np.dot(rij, rij)
    return rij2


def get_particle_energy(coordinates, box_length, i_particle, cutoff2):
    """
    This function computes the energy of a particle with the rest of the system
    """
    e_total = 0.0  # unitless energy
    i_position = coordinates[i_particle]
    particle_count = len(coordinates)
    for j_particle in range(particle_count):

        if i_particle != j_particle:

            j_position = coordinates[j_particle]
            rij2 = minimum_image_distance(i_position, j_position, box_length)
            if rij2 < cutoff2:
                e_pair = LJ_potential(rij2)
                e_total += e_pair

    return(e_total)


def calculate_total_pair_energy(coordinates, box_length, cutoff2):
    """
    calculate the total energy of the system
    """
    e_total = 0.0
    particle_count = len(coordinates)

    for i_particle in range(particle_count):
        for j_particle in range(i_particle):
            r_i = coordinates[i_particle]
            r_j = coordinates[j_particle]
            rij2 = minimum_image_distance(r_i, r_j, box_length)
            if rij2 < cutoff2:
                e_pair = LJ_potential(rij2)
                e_total += e_pair

    return e_total


def acceptance_criteron(delta_e, beta):
    """
    This function accepts or rejects a proposed move given the energy difference and system temperature

    Parameters
    ----------
    delta_e : float
        energy difference between between states after a MC move
    
    beta : float
        system temperature

    Returns
    -------
    decision : bool
        Accept or rejects a MC move
    """

    if delta_e < 0.0:
        decision = True

    else:
        random_number = np.random.rand(1)
        p_acc = np.exp(- beta * delta_e)

        if random_number < p_acc:
            decision = True
        else:
            decision = False
    
    return decision


def adjust_displacement(n_trials, n_accept, max_displacement):
    acc_ratio = float(n_accept) / float(n_trials)

    adjust_ratio = acc_ratio / 0.5

    max_displacement *= adjust_ratio

    return(max_displacement)


def main():
    
    # Testing some variables

    box_length = 10
    cutoff2 = 9
    # coordinates = generate_initial_state('random', box_length=box_length, n_particle = 800)
    coordinates = generate_initial_state('file', file_name='data/lj_sample_config_periodic1.txt')
    total_energy = calculate_total_pair_energy(coordinates, box_length, cutoff2)
    print("LJ Pair Energy :", total_energy)
    tail_correction = LJ_cutoff_correction(10, 3, 800)
    print("LJ Tail Correction Term :", tail_correction)


    #-----------------#
    # Parameter setup #
    #-----------------#

    reduced_temperature = 0.9
    reduced_density = 0.9
    n_steps = 5000
    freq = 1000
    num_particle = 100
    simulation_cutoff = 3.0
    max_displacement = 0.1
    tune_displacement = True
    build_method = 'random'

    n_trials = 0
    n_accept = 0
    energy_array = np.zeros(n_steps)
    
    # Calculate box length for given parameter set
    
    box_length = np.cbrt(num_particle / reduced_density)
    beta = 1.0 / reduced_temperature
    simulation_cutoff2 = np.power(simulation_cutoff, 2)

    #-----------------------#
    # Initialize Simulation #
    #-----------------------#

    coordinates = generate_initial_state(build_method, n_particles=num_particle, box_length=box_length)

    total_pair_energy = calculate_total_pair_energy(coordinates, box_length, simulation_cutoff2)
    tail_correction = LJ_cutoff_correction(box_length, simulation_cutoff, num_particle)

    for i_step in range(n_steps):
        
        # update the number MC move attempts
        n_trials += 1

        # select a random particle
        i_particle = np.random.randint(num_particle)

        # generates a random displacement
        random_displacement = (2.0 * np.random.rand(3) - 1.0) * max_displacement
    
        # compute energy difference of moving a single particle
        current_energy = get_particle_energy(coordinates, box_length, i_particle, simulation_cutoff2)

        proposed_coordinates = coordinates.copy()
        proposed_coordinates[i_particle] += random_displacement
        new_energy = get_particle_energy(proposed_coordinates, box_length, i_particle, simulation_cutoff2)

        delta_energy = new_energy - current_energy

        accept = acceptance_criteron(delta_energy, beta)

        if accept:
            total_pair_energy += delta_energy
            n_accept += 1
            coordinates[i_particle] += random_displacement

        total_energy = (total_pair_energy + tail_correction) / num_particle

        energy_array[i_step] = total_energy

        if np.mod(i_step + 1, freq) == 0:

            print(i_step + 1, energy_array[i_step])

            if tune_displacement:
                max_displacement = adjust_displacement(n_trials, n_accept, max_displacement)
                n_accept = 0
                n_trials = 0


if __name__ == "__main__":
    main()
