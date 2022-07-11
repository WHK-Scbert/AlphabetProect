// Generated by gencpp from file i2cpwm_board/DriveMode.msg
// DO NOT EDIT!


#ifndef I2CPWM_BOARD_MESSAGE_DRIVEMODE_H
#define I2CPWM_BOARD_MESSAGE_DRIVEMODE_H

#include <ros/service_traits.h>


#include <i2cpwm_board/DriveModeRequest.h>
#include <i2cpwm_board/DriveModeResponse.h>


namespace i2cpwm_board
{

struct DriveMode
{

typedef DriveModeRequest Request;
typedef DriveModeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct DriveMode
} // namespace i2cpwm_board


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::i2cpwm_board::DriveMode > {
  static const char* value()
  {
    return "e4da47a0d835738660a86a1db5528f89";
  }

  static const char* value(const ::i2cpwm_board::DriveMode&) { return value(); }
};

template<>
struct DataType< ::i2cpwm_board::DriveMode > {
  static const char* value()
  {
    return "i2cpwm_board/DriveMode";
  }

  static const char* value(const ::i2cpwm_board::DriveMode&) { return value(); }
};


// service_traits::MD5Sum< ::i2cpwm_board::DriveModeRequest> should match
// service_traits::MD5Sum< ::i2cpwm_board::DriveMode >
template<>
struct MD5Sum< ::i2cpwm_board::DriveModeRequest>
{
  static const char* value()
  {
    return MD5Sum< ::i2cpwm_board::DriveMode >::value();
  }
  static const char* value(const ::i2cpwm_board::DriveModeRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::i2cpwm_board::DriveModeRequest> should match
// service_traits::DataType< ::i2cpwm_board::DriveMode >
template<>
struct DataType< ::i2cpwm_board::DriveModeRequest>
{
  static const char* value()
  {
    return DataType< ::i2cpwm_board::DriveMode >::value();
  }
  static const char* value(const ::i2cpwm_board::DriveModeRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::i2cpwm_board::DriveModeResponse> should match
// service_traits::MD5Sum< ::i2cpwm_board::DriveMode >
template<>
struct MD5Sum< ::i2cpwm_board::DriveModeResponse>
{
  static const char* value()
  {
    return MD5Sum< ::i2cpwm_board::DriveMode >::value();
  }
  static const char* value(const ::i2cpwm_board::DriveModeResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::i2cpwm_board::DriveModeResponse> should match
// service_traits::DataType< ::i2cpwm_board::DriveMode >
template<>
struct DataType< ::i2cpwm_board::DriveModeResponse>
{
  static const char* value()
  {
    return DataType< ::i2cpwm_board::DriveMode >::value();
  }
  static const char* value(const ::i2cpwm_board::DriveModeResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // I2CPWM_BOARD_MESSAGE_DRIVEMODE_H
