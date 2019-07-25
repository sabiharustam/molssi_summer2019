# Use call function to create a callables that tries a move accepts or rejects and if accepts,
# update the position, bla bla

class Integrator(self, sjsjsjjsjjs):
    def ___init__(self):
        self.aa = aa


    def __call__(self):
        return

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

        return (e_total)





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

