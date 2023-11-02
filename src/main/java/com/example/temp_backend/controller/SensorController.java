package com.example.temp_backend.controller;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.model.Sensor;
import com.example.temp_backend.repository.HerstellerRepository;
import com.example.temp_backend.repository.SensorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/sensor")
public class SensorController {


    @Autowired
    SensorRepository sensorRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<Sensor> getAllSensor() {
        return sensorRepository.findAll();
    }
}
