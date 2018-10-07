echo " enter two string"
read str1
read str2
echo " 1.check if empty"
echo " 2.equality"
echo " 3.palindrome"
read test
case $test in
	1)
		if [ ! -s ${str1} ]; then
			echo " first str is not empty"
		else
			echo " first str is empty"
		fi
		if [ ! -s ${str2}  ]; then
			echo " second str is not empty"
		else
			echo " first str is empty"
		fi
		;;
	2)
		if [ ${str1} == ${str2} ];then
			echo "both are same"
		else
			echo " not same"
		fi 
		
		;;

	3)	str=$(echo "${str1}" | rev) 
		if [ ${str} == ${str1} ] ; then
			echo "palindrome"
		else
			echo "not palindrome"
		fi
		fil=$(echo "${str2}" | rev) 
		if [ ${fil} == ${str2} ] ; then
			echo "palindrome"
		else
			echo "not palindrome"
		fi
		;;	

	*)
		echo "wrong option"
		;;
  esac






