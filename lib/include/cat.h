#include "animal.h"

/// @brief Derived class representing a Cat
class Cat : public Animal {
public:
  /// @brief Implementation of the eat function for a Cat
  void eat() const override;

  /// @brief Implementation of the move function for a Cat
  void move() const override;
};
