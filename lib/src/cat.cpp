#include "cat.h"

#include <iostream>

void Cat::eat() const { std::cout << "Cat is eating" << std::endl; }

void Cat::move() const { std::cout << "Cat is moving" << std::endl; }
