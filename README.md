Role Name
=========

A relatively simple ansible role that installs all the most important packages using `pacman` module to make arch ready to be controlled by an ansible machine either locally or remotely.

Requirements
------------

There is one; a role can't specify host-specific properties like `hosts`, which is needed to interact with its ssh subsystem directly. That must be done through a play. So in any play where this role is run, the below and failry standard `raw` module task should be used if there's a chance python might not be installed:

```yaml
- name: Bootstrap python for ansible on arch-based systems
  hosts: all
  gather_facts: false
  tasks:
    - name: Install python for Ansible
      raw: test -e /usr/bin/python || (pacman --noconfirm -S python)
      become: true
      changed_when: false
```

You'll note in the `molecule` testing folder that `prepare.yml` does the same thing to prepare the vagrant instance for testing. I haven't found a way around this yet, would love suggestions that encapsulates this into a role and simplifies things.

Otherwise really the only requirement is the ability for ansible to connect, i.e. an SSH connection with the right credentials if they're needed, or to be able to run it locally.

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
