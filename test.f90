!
!++ test for call subroutine from pyton
!
!module test
!  implicit none

!  public :: hello_from_fortran

!contains
  !
  subroutine hello_from_fortran( n,   & ! IN 
                                 A    & ! IN
                               )
    
    implicit none
    integer(4), intent(in)  :: n
    real(8),    intent(in)  :: A(0:n-1,0:n-1)

    integer                 :: i, j

    write(*,*)  '   Hellow from Fortran'
    write(*,"(i8)") n
    do i = 0, n-1
      write(*,*) ( A(i,j), j=0, n-1)
    end do
    return 
  end subroutine hello_from_fortran

!end module
