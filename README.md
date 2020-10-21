# files-collector
A simple web-based tool for collecting supplementary files for presentations and speeches for the project ELITR (elitr.eu).


## How it works
`docker-compose up --build` starts the project with hot-reloading for development. `start-prod.sh` starts the project in production mode. The collected files can be found in the `collected-data` directory (the directory is bind-mounted to the container).

## Quest
The app is deployed on quest.ms.mff.cuni.cz/data-collector. Because the app doesn't live on the root path, the whole app had to be modified (to make relative links work). The modified code can be found in the `quest-deployment` branch.