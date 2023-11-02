package com.example.temp_backend.repository;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.model.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Long> {
}
