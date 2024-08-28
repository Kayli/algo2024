# algorithm excercises

- to initialize devcontainer use this guide https://code.visualstudio.com/docs/devcontainers/create-dev-container

- to autorun tests
    - install python test explorer from little fox team 
        - it can autorun pytests
        - but not integrated with default test runner
    - install RunItOn extension, as described here
        - https://python.plainenglish.io/how-to-autorun-python-tests-in-vscode-step-by-step-cfb24c6fc4be

- when adding new vscode extensions 
    - don't forget to update devcontainer.json with the following
    ```json
    {
        "customizations": {
            "vscode": {
                "extensions":[
                        "fsevenm.run-it-on", 
                        "littlefoxteam.vscode-python-test-adapter", 
                        "ryanluker.vscode-coverage-gutters"
                ]
            }
        }
    }
    ```
    - see https://www.reddit.com/r/vscode/comments/17q3mm0/what_kind_of_extensions_should_be_installed/


- to make vscode see pytest installed as dev dependency inside poetry
    - configure poetry to create venv in local workspace folder
    - point vscode to that folder by setting python.defaultInterpreterPath in vscode settings
    - see https://github.com/python-poetry/poetry/issues/108#issuecomment-628681234

- to run coverage analysis with pytest 
    - use the following command to generate lcov file
        > poetry run pytest --cov-report lcov --cov
    - use coverage gutters extension to view coverage for a file (there is a button in vscode status bar)
    - see https://pytest-cov.readthedocs.io/en/latest/reporting.html

- 'just' runner supports 
    - descriptions for targets which will be displayed by 'just -l' command
    - variadic parameters
        ```just
            commit MESSAGE *FLAGS:
                git commit {{FLAGS}} -m "{{MESSAGE}}"
        ```