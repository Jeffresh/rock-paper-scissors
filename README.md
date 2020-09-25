# Rock paper scissors
In this project you will code a Rock-Paper-Scissors-Lizard-Spock game, a more advanced version of Rock-Paper-Scissors, which can be played against the computer.

# Stage 1/5: Unfair computer

### Description

Rock, paper, scissors is a well-known hand game. Each one of two players
simultaneously forms one of three shapes with their hands, and then, depending on the chosen
shapes, the winner is determinedÑ rock beat scissors, paper wins over rock,
scissors beat paper. The game is widely used to make a fair decision between equal options.

So, let´s start with an unfair version! :)

Write a program that reads input specifying which option the user has chosen. Then your program
should make the user lose! That is, your program should always choose an option that defeats the 
one picked by the user. After finding this option, output a line ```Sorry, bu the computer chose<option>```,
where ```<option>``` is the name of option that the program picked depending on the user's input.

For example, if the user enters ```rock``` the program should print ```Sorry, but the computer chose paper``` and so son.

Please, pay attention to the format of the output. It should be exactly the same as in the example, 
including capital letteres and punctuation. No additional strings should be printed!

### Objectives

Your program should:

1. Take an input from the user
2. Find and option that wins over the user's option
3, Output a line: ```Sorry, but the computer chose <option>```

### Examples

The greater-than symbol followed by space(>) represents the user input. Notice that it's not the part
of the input.

Example 1
````bash
> scissors
Sorry, but the computer chose rock
````

Example 2

````bash
> paper
Sorry, but the computer chose scissors
````




