import re

def read_template(test_path):
    with open(test_path) as reader:
        content= reader.read()
        return content
   

def parse_template(content):

    strip_content=re.sub(r'{[^}]*}','{}', content)
    words=tuple(re.findall('{[^}]*}', content))

    list=[]

    for i in range(len(words)):
        list.append(words[i][1:-1])
    
    keys=tuple(list)

    return(strip_content,keys)

    

def merge(stripped_text,keys):
    with open("assets/make_me_a_video_game_output.txt", "w") as f:
        final_story=stripped_text.format(*keys)
        f.write(final_story)
        return final_story