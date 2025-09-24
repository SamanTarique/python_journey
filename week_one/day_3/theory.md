# if , elif , else

    - These are conditional blocks which executes only when condition turns true either its a condition/relational/character/integer
    - If there you want multiple conditions to check if one fails u can use , if - elif , here when if condition turns false then we eveluate elif conditions , and if elif also turns false it simpply skips the block and execute next statements.
    - if-elif are like if not this(if condition) then try this(elif)
    - if you want to evaluate on multiple conditions , u can chain multilple elif like,

        if a>b:
            print(f"{a}>{b}")
        elif a>c
            print(f"{a}>{c}")
        elif b>c
            print(f"{b}>{c})
        elif c>a
            print(f"{c}>{a})

    - And you you want to give a default output , if like every condition turns false then u can add a else block in chain like this,

            if a>b:
            print(f"{a}>{b}")
        elif a>c
            print(f"{a}>{c}")
        elif b>c
            print(f"{b}>{c})
        elif c>a
            print(f"{c}>{a})
        else
            print("every condition turns false")

# Logial operators (and , or , not)
    # and
        - Returns True only if both conditions are True.
    # or
        - Returns True if at least one of the conditions is True.
    # not
        - Reverses the result of the condition.
        - If the condition is True, not makes it False, and vice versa.
    
