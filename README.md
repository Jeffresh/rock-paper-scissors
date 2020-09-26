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

# Stage 2/5: Equalizing chances

### Description

Well, now let's do something real. Nobody wants the game where you always lose.
Using the power of the `random` module, we'll make a truly interesting game.

You should write a program that reads input form the user, chooses a random option and 
then says who won, the suer or the computer.

There are a few examples below, providing output for any outcome (`<option>` is the option chosen by your program):

1. Lose -> `Sorry, but the computer chose <option>`
2. Draw -> `There is a draw (<option>)`
3. Win -> `Wll done. The computer chose <option> and failed`

### Objectives

Your program should:

1. Read user's input specifying the option that user has chosen
2. Choose a random option
3. Compare the options and determine the winner
4. Output a line depending on the result of the game:
    - Lose -> `Sorry, but the computer chose <option>`
    - Draw -> `There is a draw (<option>)`
    - Win -> `Well done. The computer chose <option> and failed`

### Examples

The greater-than symbol followed by space (`>`) represents the user input. Notice
that it's not the part of the input.

#### Example 1
```
> rock
Well done. The computer chose scissors and failed
```

#### Example 2
```
> scissors
There is draw (scissors)
```

#### Example 3
```
> paper
Sorry, but the computer chose scissors
```

# Stage 3/5: Endless game

### Description

Wasn't that pretty cool?

But the game is really short so far: nobody plays just a single shot of rock-paper-scissors.
We need to do some literally unstoppable game for unstoppable players. Not literally unstoppable, of course:
let's implement a way to stop your program.

Improve your program so it would take an unlimited number of inputs until the user enters
`!exit`. After entering `!exit` the program should print `Bye!` and terminate. Also, let's try to handle invalid inputs:
your program should be ready that there many be a type in user's input, or that a user may just enter complete gibberish
instead of a normal command. So, in case the input doesn't correspond to any known command (option name or `!exit`), your
program should output the line `Invalid input`

### Objectives

Your program should:

1. Take an input from the user
2. If the input is `!exit`, output `Bye!` and stop the game
3. If the input is the name of the option, then:
    1. Pick a random option
    2. Output a ine with the result of the game in following format(`<option>` is the name of the option chosen by the program):
        - Lose -> `Sorry, but the computer chose <option>`
        - Draw -> `There is a draw (<option>)`
        - Win -> `Wel done. The computer chose <option> and failed`
4. If the input corresponds to anything else, output `Invalid input`
5. Do it all over again

### Examples

The greater-than symbol followed by space (`>`) represents the user input. Notice that it's not the part
of the input.
```
> rock
Well done. The computer chose scissors and failed
> paper
Well done. The computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but the computer chose rock
> rokc
Invalid input
> xit!
Invalid input
> !exit
Bye!
```