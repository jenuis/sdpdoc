.. user_environment

User Environment 
=====================

---------------------------
Linux OS
---------------------------

The SDP server is installed with AlmaLinux OS. We assume that you already have the basic knowledge of Linux. If not, you can refer to the listed websites to learn more. 

- `The Missing Semester of Your CS Education <https://missing.csail.mit.edu/>`_ (Videos lectures on `Youtube <https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J>`_ or `Bilibili <https://www.bilibili.com/video/BV1x7411H7wa/?vd_source=30c24d7b396c267c57a25dabb6d5d248>`_)
- `Linux简单教程 <https://www.runoob.com/linux/linux-tutorial.html>`_ 

---------------------------
Environment Modules
---------------------------

In Linux, different user may use different version of applications or libraries. To simplify the initialization of the shell environment, the `Environment Modules <https://modules.sourceforge.net/>`_ is normally used. The SDP employs a new environment module system, namely the Lua based module system (`Lmod <https://lmod.readthedocs.io/en/latest/index.html>`_) to simplify the usage of the module commands.

To view all the available modules, use ``module avail`` (or ``ml av`` for Lmod):

.. code-block:: bash

    [xiangliu@localhost ~] module avail
    ------------------------------ /work/IDE/modulefiles ----------------------------------------
    IDE/MATLAB/R2020a    IDE/MATLAB/R2020b (D)    IDE/PyCharm/2021.3    IDE/PyCharm/2022.3 (D)
    [xiangliu@localhost ~] ml av
    ------------------------------ /work/IDE/modulefiles ----------------------------------------
    IDE/MATLAB/R2020a    IDE/MATLAB/R2020b (D)    IDE/PyCharm/2021.3    IDE/PyCharm/2022.3 (D)

To load a module, use ``module load module-name`` (or ``ml module-name`` for Lmod):

.. code-block:: bash

    [xiangliu@localhost ~] module load IDE/MATLAB
    [xiangliu@localhost ~] ml IDE/PyCharm

To view the loaded modules, use ``module list`` (or ``ml`` for Lmod):

.. code-block:: bash

    [xiangliu@localhost ~] module list
    Currently Loaded Modules:
      1) IDE/MATLAB/R2020b   2) IDE/PyCharm/2022.3
    [xiangliu@localhost ~] ml
    Currently Loaded Modules:
      1) IDE/MATLAB/R2020b   2) IDE/PyCharm/2022.3

Correspondingly, to unload a module use ``module unload module-name`` (or ``ml unload module-name``):

.. code-block:: bash

    [xiangliu@localhost ~] module unload IDE/MATLAB
    [xiangliu@localhost ~] ml
    Currently Loaded Modules:
      1) IDE/PyCharm/2022.3
    [xiangliu@localhost ~] ml unload IDE/PyCharm

To unload all the modules, use ``module purge`` (or ``ml purge``):

.. code-block:: bash

    [xiangliu@localhost ~]$ ml purge
    [xiangliu@localhost ~]$ ml
    No modules loaded

---------------------------
User Bash Profile
---------------------------

The bash profile is automatically loaded when a shell session is established. If you want certain modules to be loaded automatically, please insert the command into your bash profile (**.bashrc**). For instance, MATLAB can be used directly once you login the SDP, if you have done the following.

.. code-block:: bash

    [xiangliu@localhost ~] vi ~/.bashrc
    # .bashrc

    # User specific aliases and functions
    module load MATLAB
