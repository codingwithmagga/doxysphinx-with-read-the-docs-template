#include "animal.h"

/// @brief Derived class representing a Dog
class Dog : public Animal {
public:
  /// @brief Implementation of the eat function for a Dog
  void eat() const override;

  /// @brief Implementation of the move function for a Dog
  void move() const override;
};
