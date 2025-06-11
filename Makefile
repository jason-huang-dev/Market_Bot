build:
	echo "Building bot..."
	pip install -r requirements.txt

deploy:
	echo "Deploying bot..."
	python3 -m market_bot

build-and-deploy: build deploy
