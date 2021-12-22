program TestProgram

use Declination_angle

implicit none

real(4) ::dangle
integer ::mon, day

mon=4
day=7

call calculate_angle(mon,day,dangle)

write(*,*) dangle

end program TestProgram