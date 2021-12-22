program Test

use solar_hour_angle

implicit none

real(4) :: t,lon,angle
integer :: mon,day

t=9
lon=56.43
mon=4
day=7

call calculation(lon,mon,day,t,angle)

write(*,*) angle

end program Test