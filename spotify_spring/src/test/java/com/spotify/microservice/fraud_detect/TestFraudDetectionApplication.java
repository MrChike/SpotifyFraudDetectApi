package com.spotify.microservice.fraud_detect;

import org.springframework.boot.SpringApplication;

public class TestFraudDetectionApplication {

	public static void main(String[] args) {
		SpringApplication.from(FraudDetectionApplication::main).with(TestcontainersConfiguration.class).run(args);
	}

}
