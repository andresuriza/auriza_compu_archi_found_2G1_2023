module PSregister(input reg[3:0] msj,
						input clk, load,
						output data);
						
		 logic And1, And2, And3, And4, And5, And6, And7, Or1, Or2, Or3;
		 wire Q1, Q2, Q3, Q4;
		 
		 assign And1 = (msj[0])&~load;
		 
		 flipflop f1(And1, clk, Q1);
		 
		 assign And2 = Q1&load;
		 assign And3 = ~load&(msj[1]);
		 assign Or1 = And2|And3;
		 
		 flipflop f2(Or1, clk, Q2);
		 
		 assign And4 = Q2&load;
		 assign And5 = ~load&(msj[2]);
		 assign Or2 = And4|And5;
		 
		 flipflop f3(Or2, clk, Q3);
		 
		 assign And6 = Q3&load;
		 assign And7 = ~load&(msj[3]);
		 assign Or3 = And6|And7;
		 
		 flipflop f4(Or3,clk,Q4);
		 
		 assign data = Q4;
		 

	

endmodule