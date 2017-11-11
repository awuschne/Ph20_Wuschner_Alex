.PHONY : pngs
pngs: Pset3_py.py 1.png 2.png 3.png 4.png 5.png 6.png 7.png 8.pngs 9.png 10.png 11.png 12.png 13.png

1.png : Pset3_py.py
	python $^ $@
2.png : Pset3_py.py
	python $^ $@
3.png : Pset3_py.py
	python $^ $@
4.png : Pset3_py.py
	python $^ $@
5.png : Pset3_py.py
	python $^ $@
6.png : Pset3_py.py
	python $^ $@
7.png : Pset3_py.py
	python $^ $@
8.png : Pset3_py.py
	python $^ $@
9.png : Pset3_py.py
	python $^ $@
10.png : Pset3_py.py
	python $^ $@
11.png : Pset3_py.py
	python $^ $@
12.png : Pset3_py.py
	python $^ $@

13.png : Pset3_py.py
	python $^ $@

.PHONY : clean
clean:
	rm -f *.png