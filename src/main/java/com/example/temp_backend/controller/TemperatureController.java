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
    public @ResponseBody Iterable<Temperature> getTemperatureBySensorId(@PathVariable Long id) {
        return temperatureRepository.findBySensorId(id);
    }
    @GetMapping(path = "/getLastTemp/{id}")
    public @ResponseBody Iterable<Temperature> getLast10TemperatureBySensorId(@PathVariable Long id) {
        return temperatureRepository.findLast10TempBySensorId(id);
    }
    @GetMapping(path = "/getMaxTemp/{id}")
    public @ResponseBody Iterable<Temperature> getMaxTemperatureBySensorId(@PathVariable Long id) {
        return temperatureRepository.findMaxTempBySensorId(id);
    }
    @GetMapping(path = "/getAvgTemp/{id}")
    public @ResponseBody Iterable<Temperature> getAvgTemperatureBySensorId(@PathVariable Long id) {
        return temperatureRepository.findAvgTempBySensorId(id);
    }

    @DeleteMapping("/{id}")
    void deleteSensor(@PathVariable Long id) {
        temperatureRepository.deleteById(id);
    }


}
