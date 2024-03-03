import yaml
import re
import time

template_file_path = r"template-file.html" #leave the r 
template_filler_path = r"filler.yaml"  #leave the r !! .yaml
replace_pattern = r'\{\{([^{}]+)\}\}' #REGEX for what to replace. Deafult is {{variable}}
file_title = "../public_www/blog/article/" + str(int(time.time())) + "-blog.html" #set title and directory of output

with open(template_filler_path, "r") as template_filler:
    yaml_thing = yaml.safe_load(template_filler)
print (yaml_thing)

with  open(template_file_path, "r") as template_file:
    template_file_content = template_file.read()
    result_string = re.sub(replace_pattern, lambda match: yaml_thing.get(match.group(1), match.group(0)), template_file_content)


with open (file_title, "w") as write_file:
    write_file.write(result_string)