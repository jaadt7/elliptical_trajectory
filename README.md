[![DOI](https://zenodo.org/badge/476419216.svg)](https://doi.org/10.5281/zenodo.14796676)

# elliptical_trajectory

The interpulse time in Thermal Pulsing Asymptotic Giant Branch (TP-AGB) stars is of utmost importance to nuclear astrophysicists as it is where the main branch of the s-process occurs. The variation of the neutron flux as a function of temperature in the time between the pulses from the MESA code is used as the template for the parametrization, and an elliptical trajectory was deemed most appropriate.

This repository aims to create approximate trajectories to mimic those that occur in TP-AGB stars. As stellar codes can take a very long time to run. The trajectory_builder notebook can create an approximative trajectory one could use to run preliminary s-process type calculations, or others of interest.

The first notebook, trajectory_builder, takes three input coordinates in that space, approximates an elliptical trajectory, and saves the data to file. The notebook itself contains all the documentation required to run it. You can download it and run it locally, or run it on Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jaadt7/elliptical_trajectory/blob/master/trajectory_builder.ipynb)

The second notebook, gallery, is a duplicate of trajectory_builder in terms of built-in functions. It contains images and animations showcasing some trajectories of interest. As the first, you can simply download it and run it locally, or run it on Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jaadt7/elliptical_trajectory/blob/master/gallery.ipynb)
