bingame
=======

A small game in which the player converts a number to binary.

What it needs
=============
This game requires Python 2.7 on your system. Most Linux distributions include this out of the box, but if not, you can install it from your package manage if your distro has one. Windows and Mac OSX users will need to download it from python.org/download and install it on your system. Be sure to pick the right download for your operating system and processor architecture and remember, version 2.7, not 3.

How to run
==========

Extract the contents of this ZIP file somewhere you can easily find it, for example, your home folder (if using Linux) or your C:\ drive (if using Windows). Make sure to extract ALL files when you do so. It's so easy to get caught out by your ZIP program and wind up extracting only the selected file. Done that? Great.

Open a command prompt (Windows) or terminal window (Linux/Mac OSX) and navigate to the correct folder using "dir" (Windows) or "cd" (Linux/Mac). Once there, type "python bingame.py" and it should run. Otherwise, I don't know what to say.

How to play
===========

You're given a number, which must be converted to binary. To do this, you need to divide the number given by two, provide the answer rounded down (not up) to the nearest whole number, as well as the remainder, and then divide the answer by two and so on. If the original result of each division before rounding down is a decimal number, the remainder is always 1. If it's a whole number, then the remainder is 0. An easy way to help is to look at the final digit of the number you are dividing. Dividing odd numbers will always result in a remainder of 1 while even numbers will result in a 0.

After reaching a point where you can divide no more, you will be asked to enter the binary value of that number. To do this, just recite the remainders of every number you divided in reverse order. That means, start from the last remainder you found and work your way back up. When you've got it right you will be graded on the number of errors you've made. Try to get a PERFECT grade, but don't worry if you end up with an X. Binary's confusing, but the more practice you get the more it'll make sense.
