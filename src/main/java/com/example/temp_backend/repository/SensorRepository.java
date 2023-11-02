package com.example.temp_backend.repository;

import com.example.temp_backend.model.Sensor;
import org.springframework.data.repository.CrudRepository;

public interface SensorRepository extends CrudRepository<Sensor, Long> {
}
