package com.example.temp_backend.controller;

import com.example.temp_backend.model.Temperature;
import com.example.temp_backend.repository.TemperatureRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/temperature")
public class TemperatureController {
    @Autowired
    TemperatureRepository temperatureRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<Temperature> getAllTemperature() {
        return temperatureRepository.findAll();
    }

    @GetMapping(path = "/{id}")
    public @ResponseBody Iterable/**/<Temperature> getTemperatureBySensorId(@PathVariable Long id) {
        return temperatureRepository.findBySensorId(id);
    }

    @PostMapping
    Temperature insertTemperature(@RequestBody Temperature newTemperature) {
        return temperatureRepository.save(newTemperature);
    }

    @DeleteMapping("/{id}")
    void deleteSensor(@PathVariable Long id) {
        temperatureRepository.deleteById(id);
    }


}
