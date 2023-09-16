from setuptools import find_packages, setup

# Define the path to the requirements file
requirement_filePath = 'requirements.txt'
editable_indicator = '-e .'

def get_requirements():
    with open(requirement_filePath) as requirementFile:
        requirement_list = requirementFile.readlines()
    requirement_list = [requirement.replace("\n", "") for requirement in requirement_list]
    
    # Remove the editable_indicator from the requirements
    if editable_indicator in requirement_list:
        requirement_list.remove(editable_indicator)
    
    return requirement_list

setup(
    name='custom_chatbot',
    version='0.0.1',
    description='Fully flexible custom chatbot.',
    author='Jyoti Kapoor',
    author_email='jyotikpr999@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
