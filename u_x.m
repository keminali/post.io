filename='v.csv';   % assign file to a variable
m=csvread(filename);  %Read comma-separated value (CSV) file 
u=m(:,1);            % extract first column data, i.e. U_x
u=u.' ;     %change column vector to row vector (transpose)
u_x=fliplr(u);    % change orders of array, Flip array left to right
u_x=u_x.';          %  change row vector back to column vector (transpose)
u_0=1102.9;       % jet exit velocity
u_x_nor=u_x/u_0;  % normalize axial veloicty
x=m(:,5) ;      % extract 5th column data, i.e. x coordinates
d=0.0025;      % diameter of jet
x_nor=x/d;       % normalize axial distance
plot(x_nor, u_x_nor) ;
xlabel('X/D');
ylabel('U_{C}/U_{J}');
print -deps u_x.eps ; % save plot as eps image 
output=[u_x_nor x_nor]; % format a matrix
save -ascii u_vs_x.txt output; 

