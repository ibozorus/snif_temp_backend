package com.example.temp_backend.repository;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.model.Temperature;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface TemperatureRepository extends CrudRepository<Temperature, Long> {
    @Query("SELECT a FROM Temperature a WHERE a.sensor.id = ?1")
    Iterable<Temperature> findBySensorId(Long id);
    @Query("SELECT a.value FROM Temperature a WHERE a.sensor.id = ?1 ORDER BY a.timestamp DESC LIMIT 10")
    Iterable<Temperature> findLast10TempBySensorId(Long id);
    @Query("SELECT a FROM Temperature a WHERE a.sensor.id = ?1 ORDER BY a.value DESC LIMIT 1")
    Iterable<Temperature> findMaxTempBySensorId(Long id);
    @Query("SELECT AVG(a.value) AS avg_temp FROM Temperature a WHERE a.sensor.id = ?1")
    Iterable<Temperature> findAvgTempBySensorId(Long id);
}
