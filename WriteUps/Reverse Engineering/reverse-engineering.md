# Reverse Engineering Writeup

## #1 hackerman
![](https://i.imgur.com/O2DtsZJ.png)

Given challenge file is a 64 bit ELF binary which is the standard file format for executable files in unix based systems.

![](https://i.imgur.com/wGFaVnO.png)

We can execute binaries with `./filename`

If we try to execute the binary, it prompts for a passcode that we don't know yet. 

![](https://i.imgur.com/OrYGAa5.png)

Our task is to find the passcode and get the flag!

Luckily, we have a command called `strings` which can print readable characters in a binary file.

![](https://i.imgur.com/o80mEbp.png)

Let's see the strings in this binary file using `strings` command.

![](https://i.imgur.com/slQgHfq.png)

As we can see there is a string "hail_hydra" just after the passcode prompt. So let's try to use this as the passcode.

![](https://i.imgur.com/HoEThed.png)

And here we go! We got the flag.

## #2 easy_python
![](https://i.imgur.com/Dppz91q.png)

For this challenge we have a python file but if we try to run it with newer versions of python (3.10.1 as of now), it gives us SyntaxError.

![](https://i.imgur.com/dmF8Y7l.png)

So now, as the challenge says, python3.8 can execute this file. Let's try to execute this with python3.8

![](https://i.imgur.com/qclq99p.png)

Now we have to find prime factors of this huge number.

Doing this in python would take a lot of time because this value is very big, so let's use some online tool for this.

In this case, I'm using `dcode.fr` because it works fine with big values.

And as you can clearly see, we got two prime factors of the number.

![](https://i.imgur.com/aluO0F1.png)

Entering those two factors in the program gives us the flag.

![](https://i.imgur.com/7NbZFWg.png)