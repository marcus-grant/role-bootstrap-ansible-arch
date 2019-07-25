Role Name
=========

A relatively simple ansible role that installs all the most important packages using `pacman` module to make arch ready to be controlled by an ansible machine either locally or remotely.

Requirements
------------

Really the only requirement is the ability for ansible to connect, i.e. an SSH connection with the right credentials if they're needed, or to be able to run it locally.

Role Variables
--------------

### TODO

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

- None

Example Playbook
----------------

### TODO

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: bootstrap-ansible-arch, x: 42 }

License
-------

CC-BY

Author Information
------------------

- Marcus Grant
- marcusfg@gmail.com
