def get_input(word):
    user_input = input(f'Enter a {word}:')
    return user_input


name1 = get_input("name")
verb1 = get_input("verb")
name2 = get_input("name")
verb2 = get_input("verb")

story = f"""
Title: The Python Programmer's Dilemma
[Scene: A programmer's desk. {name1} is sitting in front of his computer, scratching his head, while his code runs.]
{name1}: [Muttering to himself] Why isn't this working? I've checked the syntax a hundred times!
[Enter {name2},{name1}'s programmer friend, holding a cup of coffee.]
{name2}: Hey,{name1}! What's the problem?
{name1}: Hey,{name2}. I'm trying to debug this code, but I can't figure out what's causing the issue.
{name2}: Mind if I take a look?
{name1}: Please, be my guest.
[{name2} starts examining the code, sips his coffee, and suddenly gets an idea.]
{name2}: Ah-ha! I think I've found the culprit!
{name1}: Really? What is it?
{name2}: It looks like you've summoned a {verb1} instead of a variable!
{name1}: Wait, what? How did that happen?
{name2}: It seems you accidentally named your variable "{verb2}" instead of "{verb1}"
{name1}: Oh no, not again! My fingers must have had a mind of their own!
{name2}: Don't worry, we'll fix it together. We just need to perform the sacred ritual of renaming.
[{name1} and {name2} gather around the computer, holding hands dramatically.]
{name1}: Oh mighty Python gods, grant us your forgiveness and bless this code with clarity!
{name2}: Let the power of Ctrl+C and Ctrl+V be with us!
[{name1} and {name2} simultaneously press the Ctrl key and perform the sacred copy-paste motion.]
{name1}: [Eagerly] Did it work?
{name2}: [Checks the code] It seems we've successfully banished the {verb1} and summoned the rightful variable, "{verb2}"!
[They both high-five each other.]
{name1}: You're a lifesaver, {name2}! I owe you a cup of coffee.
{name2}: Make it two cups, and we'll call it even!
[They laugh and continue coding, with renewed determination.]
End of Story
"""
print(story)
