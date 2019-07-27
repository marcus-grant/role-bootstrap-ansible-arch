To-Do's
=======

In-Progress
-----------

- [ ] Fill in the meta document with all the expected ansible role info


Planning
--------


Future
------

- [ ] Figure out if there's a way to put the `raw` ssh command to install python into the role itself
- [ ] Add other AUR helpers support, for now it's just `yay` & 'makepkg'
- [ ] Add enabler variable that specifies if aur is to be used at all

Completed
---------

- [x] Add variable that specifies which aur module to install
- [x] Add condition for default var checking if should install aur ansible module
- [x] Add conditions that check for aur helper install to skip those tasks
- [x] Install an aur helper, default to `yay`
- [x] Install base arch packages to use `makepkg`
- [x] Upgrade packages task with false default var as condition to do it
- [x] Install aur helper
- [x] Install aur_builder ansible module to local ansible configs to make dealing with arch remotes easier
- [x] Give `aur_builder` user sudoers access only to pacman to update aur packages
- [x] Install git
- [x] Install wget
- [x] Install curl
- [x] `aur_builder` user task for getting around the non-root requirement for using AUR packages
- [x] Set molecule platform to `archlinux/archlinux`
- [x] Finish setting up the molecule test environment