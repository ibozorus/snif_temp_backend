package com.example.temp_backend.controller;

import com.example.temp_backend.model.ChangeLog;
import com.example.temp_backend.repository.ChangeLogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping(path = "/changelog")
public class ChangeLogController {

    @Autowired
    ChangeLogRepository changeLogRepository;

    @GetMapping(path = "/all")
    public @ResponseBody Iterable<ChangeLog> getAllChangeLog() {
        return changeLogRepository.findAll();
    }

    @GetMapping(path = "/{id}")
    public @ResponseBody Optional<ChangeLog> getChangeLogById(@PathVariable Long id) {
        return changeLogRepository.findById(id);
    }

    @PostMapping
    ChangeLog insertChangeLog(@RequestBody ChangeLog newChangeLog) {
        return changeLogRepository.save(newChangeLog);
    }

    @PutMapping("/{id}")
    ChangeLog replaceChangeLog(@RequestBody ChangeLog newChangeLog, @PathVariable Long id) {

        return changeLogRepository.findById(id)
                .map(ChangeLog -> {
                    ChangeLog.setUser(newChangeLog.getUser());
                    ChangeLog.setSensor(newChangeLog.getSensor());
                    return changeLogRepository.save(ChangeLog);
                })
                .orElseGet(() -> {
                    newChangeLog.setId(id);
                    return changeLogRepository.save(newChangeLog);
                });
    }

    @DeleteMapping("/{id}")
    void deleteChangeLog(@PathVariable Long id) {
        changeLogRepository.deleteById(id);
    }

}
