package com.example.temp_backend.controller;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.repository.HerstellerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/hersteller")
public class HerstellerController {

    @Autowired
    HerstellerRepository herstellerRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<Hersteller> getAllHersteller() {
        return herstellerRepository.findAll();
    }
    @GetMapping(path = "/{id}")
    public @ResponseBody Optional<Hersteller> getHerstellerById(@PathVariable Long id) {
        return herstellerRepository.findById(id);
    }

    @PostMapping
    Hersteller insertHersteller(@RequestBody Hersteller newHersteller) {
        return herstellerRepository.save(newHersteller);
    }

    @PutMapping("/{id}")
    Hersteller replaceHersteller(@RequestBody Hersteller newHersteller, @PathVariable Long id) {

        return herstellerRepository.findById(id)
                .map(Hersteller -> {
                    Hersteller.setBrand(newHersteller.getBrand());
                    return herstellerRepository.save(Hersteller);
                })
                .orElseGet(() -> {
                    newHersteller.setId(id);
                    return herstellerRepository.save(newHersteller);
                });
    }

    @DeleteMapping("/{id}")
    void deleteHersteller(@PathVariable Long id) {
        herstellerRepository.deleteById(id);
    }

}
