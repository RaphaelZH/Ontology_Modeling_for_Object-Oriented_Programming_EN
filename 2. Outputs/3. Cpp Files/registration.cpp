#include <string>

class School
{
private:
    std::string id = "";
private:
    std::string name = "";

public:
    std::string get_id() const
    {
        return id;
    }

public:
    std::string get_name() const
    {
        return name;
    }

public:
    void set_id(const std::string &value)
    {
        id = value;
    }

public:
    void set_name(const std::string &value)
    {
        name = value;
    }

};class Student
{
private:
    std::string id = "";
private:
    std::string name = "";

public:
    std::string get_id() const
    {
        return id;
    }

public:
    std::string get_name() const
    {
        return name;
    }

public:
    void set_id(const std::string &value)
    {
        id = value;
    }

public:
    void set_name(const std::string &value)
    {
        name = value;
    }

};class Class
{
private:
    std::string id = "";
private:
    std::string name = "";

public:
    std::string get_id() const
    {
        return id;
    }

public:
    std::string get_name() const
    {
        return name;
    }

public:
    void set_id(const std::string &value)
    {
        id = value;
    }

public:
    void set_name(const std::string &value)
    {
        name = value;
    }

};