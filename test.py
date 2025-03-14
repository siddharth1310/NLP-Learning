import yaml

with open("nlp_course_env.yml", "r") as file:
    env_data = yaml.safe_load(file)

requirements = []

for dep in env_data.get("dependencies", []):
    if isinstance(dep, str):
        requirements.append(dep.split("=")[0])  # Remove version constraints
    elif isinstance(dep, dict) and "pip" in dep:
        requirements.extend(dep["pip"])

with open("requirements.txt", "w") as req_file:
    req_file.write("\n".join(requirements))

print("requirements.txt generated successfully!")
