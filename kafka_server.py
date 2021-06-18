import producer_server

KAFKA_TOPIC_NAME = "sf.police.callsforsvc"
BOOTSTRAP_SERVER = "localhost:9092"
CLIENT_ID = "sf.crime.stats"

def run_kafka_server():
	# TODO get the json file path
    input_file = "./police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=KAFKA_TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVER,
        client_id=CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
