#include <string>

class A1
{
private:
    std::string a1 = "";

public:
    std::string get_A1() const
    {
        return a1;
    }

    void set_A1(const std::string &value)
    {
        a1 = value;
    }
};