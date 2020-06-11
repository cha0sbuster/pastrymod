# pastrymod
Library/template project for life sim games in Ren'Py.
Pastrymod is a half-library, half-template for simulator authors, focused on dealing with most of the heavy code lifting for creating extensible, maintainable, powerful simulations.

The challenge with writing simulations in Ren'Py is that it's not meant for heavily forked, self-interacting experiences, so without significant effort, it quickly becomes too much to reasonably maintain. Many projects go silent because their source code becomes so bloated (excuse the turn of phrase) that it becomes intimidating to LOOK at.

By hiding enough of the code behind the scenes but allowing full access and tweaking, Pastrymod will allow you to implement characters, races, items, locations and interactions by writing plain .JSON -- a powerful, human-readable data storage format. By compartmentalizing content, files become leaner and easier to read, parse and edit, saving hours of work with maintenance.

Development has only just started, so it's currently nothing more than a half-functional JSON parser, but if you know Python and you want to help, I'd appreciate it!
