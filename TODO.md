To-Do's
=======

In-Progress
-----------

- [ ] Install git
- [ ] Install wget
- [ ] Install aur_builder ansible module to local ansible configs to make dealing with arch remotes easier


Planning
--------

- [ ] Install aur helper
- [ ] Fill in the meta document with all the expected ansible role info

Future
------

- [ ] Figure out if there's a way to put the `raw` ssh command to install python into the role itself
- [ ] Add other AUR helpers support, for now it's just `yay`

Completed
---------

- [x] Install curl
- [x] `aur_builder` user task for getting around the non-root requirement for using AUR packages
- [x] Set molecule platform to `archlinux/archlinux`
- [x] Finish setting up the molecule test environment