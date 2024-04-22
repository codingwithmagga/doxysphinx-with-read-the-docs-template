/// @brief Abstract Animal class
class Animal {
public:
  /// @brief Pure virtual function to represent eating behavior of an animal
  virtual void eat() const = 0;

  /// @brief Pure virtual function to represent moving behavior of an animal
  virtual void move() const = 0;
};
