Role Name
=========

A relatively simple ansible role that installs all the most important packages using `pacman` module to make arch ready to be controlled by an ansible machine either locally or remotely.

Check the `TODO.md` file in the repository to get an idea of what has been finished and what is planned. I'll respond to issues and pull requests as well.

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

* `arch_bootstrap_upgrade_pkgs`
  * default: `false`
  * whether this role should start by upgrading all pacman packages and its package cache
* `aur_use_helper`
  * default: `true`
  * if the remote should enable an AUR helper to install AUR packages
* `aur_helper`
  * default: `yay`
  * the AUR helper to install and use
* `arch_bootstrap_install_ansible_aur_mod`
  * default: `true`
  * will or won't install the [ansible-aur][01] ansible module
* `arch_bootstrap_aur_mod_ver`
  * default: `v0.23`
  * the default git version tag to checkout of the [ansible-aur][01] module

Dependencies
------------

- None

Example Playbook
----------------

### Note

* This must be used on an arch-based distribution, *i.e. one that uses pacman as its package manager*
  * Arch, Antergos, Manjaro are all valid examples
* Because AUR needs to be run by a **non-root** user, this role creates a user `aur_builder`
  * Anytime you use the `aur` module you must use the `become_user: aur_builder` property
* **NOTE** `yay` is the only helper implemented so far, if people ask for an implementation of installing another AUR helper, I'll probably do it.
* I'll also definitely accept pull requests
* Arch can get sketchy when package upgrades are done, try to only use the `arch_bootstrap_upgrade_pkgs` variable on relatively fresh systems
* Remember that installing the ansible aur module will only work on an arch machine

```yaml
- hosts: machines
  roles:
    - { role: bootstrap-ansible-arch, arch_bootstrap_upgrade_pkgs: true }
```

License
-------

CC-BY

Author Information
------------------

- Marcus Grant
- marcusfg@gmail.com

[01]: https://github.com/kewlfft/ansible-aur "Ansible AUR Module"