package com.example.temp_backend.controller;

import com.example.temp_backend.model.Sensor;
import com.example.temp_backend.repository.SensorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/sensor")
public class SensorController {
    @Autowired
    SensorRepository sensorRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<Sensor> getAllSensor() {
        return sensorRepository.findAll();
    }

    @GetMapping(path = "/{id}")
    public @ResponseBody Optional<Sensor> getSensorById(@PathVariable Long id) {
        return sensorRepository.findById(id);
    }

    @PostMapping
    Sensor insertSensor(@RequestBody Sensor newSensor) {
        return sensorRepository.save(newSensor);
    }

    @PutMapping("/{id}")
    Sensor replaceSensor(@RequestBody Sensor newSensor, @PathVariable Long id) {

        return sensorRepository.findById(id)
                .map(Sensor -> {
                    Sensor.setSensorAddress(newSensor.getSensorAddress());
                    Sensor.setHersteller(newSensor.getHersteller());
                    Sensor.setMaxTemp(newSensor.getMaxTemp());
                    Sensor.setServerCabin(newSensor.getServerCabin());
                    return sensorRepository.save(Sensor);
                })
                .orElseGet(() -> {
                    newSensor.setId(id);
                    return sensorRepository.save(newSensor);
                });
    }

    @DeleteMapping("/{id}")
    void deleteSensor(@PathVariable Long id) {
        sensorRepository.deleteById(id);
    }


}
