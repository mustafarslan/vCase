# vCase

## Prerequisite
To run tests, please run following command:
```
  pip install -r requirements.txt
```


## Build & Run with Docker
To create an image, please run following command: 
```
    docker build -t vcase . 
```

To run newly create image, please run following command:
```
    docker run vcase
```

## Tests
To run pytest
- Change your current directory to "vCase"
- Then run following command:
    ```
        pytest
    ```