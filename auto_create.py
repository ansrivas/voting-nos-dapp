# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize module utils."""

import subprocess


def execute_subprocess(cmd):
    """Execute a subprocess and return its exit status."""
    status = 0
    try:
        print("Executing process: {0}".format(cmd))
        status = subprocess.check_call(cmd, shell=True)
    except Exception as ex:
        status = ex.returncode
    return status


def main():
    """Execute the setup steps."""
    # Check if docker-compose file has our substring
    submodule_init_cmd = 'git submodule update --init --recursive'
    if 0 != execute_subprocess(submodule_init_cmd):
        raise Exception("Failed to clone subdirectories")

    print("Appending current smart-contract directory to docker-compose file...")

    with open('nos-local/neo-local/docker-compose.yml', 'r') as f:
        docker_compose_content = f.readlines()

    check_line = ["      - ../../custom-smart-contracts:/custom-smart-contracts\n",
                  "      - ../contracts:/nos-smart-contract\n"]

    add_after_line = "      - ./smart-contracts:/smart-contracts\n"

    print("Checking if directory already exists...")
    for idx, line in enumerate(check_line):
        if line not in docker_compose_content:
            index = docker_compose_content.index(add_after_line)
            print("Directory does not exist. Will append now")
            docker_compose_content = docker_compose_content[0:index+idx+1] + [line] + docker_compose_content[index+idx+1:]
            with open('nos-local/neo-local/docker-compose.yml', 'w') as f:
                for new_line in docker_compose_content:
                    f.write(new_line)
            print("Successfully appended current smart contract directory to docker-compose")
        else:
            print("Our smart contract directory is already mapped volume in docker-compose..")

    docker_compose_up_cmd = "docker-compose -f nos-local/neo-local/docker-compose.yml up -d"
    if 0 != execute_subprocess(docker_compose_up_cmd):
        raise Exception("Failed to execute: {0}".format(docker_compose_up_cmd))


if __name__ == '__main__':
    main()
