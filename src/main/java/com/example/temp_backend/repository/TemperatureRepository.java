package com.example.temp_backend.repository;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.model.Temperature;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface TemperatureRepository extends CrudRepository<Temperature, Long> {
    @Query("SELECT a FROM Temperature a WHERE a.sensor.id = ?1")
    Iterable<Temperature> findBySensorId(Long id);
}
