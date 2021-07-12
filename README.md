# mpm
Potentially saner way of managing max projects and making sharing simpler.

This repo is an experiment in thinking about packamge management for Max. We have npm, cargo, pip for managing the dependencies but for Max there is just a utility for installing global packages. Often when I want to send a project to someone those global package versions differ, or they don't have externals/abstractions/data to go along with what I want to send them. Projects are one answer to this problem, but they have their own warts. Ideally something revolving around a lock file, and conventions for establishing versions of abstractions and other packages would make an ideal system for composing projects of dependencies.

As it stands, this experiment takes a top-level patcher, collects the dependencies and creates a new unstrucred folder that anyone should be able to open and use in Max. 

Fundamentally, I do not think the issue can be solved until I fully figure out how to programatically create Max projects that localise all dependencies.
