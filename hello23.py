import streamlit  as st
st.header(" WELCOME TO POLYTECHNIC  GOVERNMENT CHAMARAJANAGAR ")
st.image("govtpolychamraj01.jpg")
st.container()
st.write("SECOND SEM RESULTS")
button=st.button("GET RESULT")
if button==True:
   table="""<table border="1">
<th> regno </th>
<th> name</th>
<th> sem </th>
<th> pms</th>
<th> s_and_a</th>
    <th>c_s</th>
    <th>caeg</th>
    <th>m_and_a</th>
    <th>total</th>
        <th>result</th>
<tr>
    <td>130CS21003</td><td>	AISHWARYA M</td><td>	2</td><td>	11</td>	<td>32</td>	<td>35</td>	<td>20</td>	<td>27</td>	<td>326</td>	<td>FAIL</td></tr>
 <tr>   <td>130CS21005</td><td>AMITH G S</td><td>	2</td></td><td>	35	</td><td>36</td>	<td>37</td>	<td>29</td>	<td>34</td>	<td>419</td>	<td>Distinction</td></tr>
   <tr> <td>130CS21006</td>	<td>AMRUTHA L</td><td>	2</td>	<td>23</td><td>	31</td><td>	34</td><td>	16</td><td>	28</td>	<td>364</td>	<td>First Class</td></tr>
	<tr><td>130CS21007</td>	<td>AMRUTHA M</td><td>	2</td><td> 14</td><td>	30</td><td>	33</td><td>	8</td><td>	20</td><td>	290</td>	<td>FAIL</td></tr>
	<tr><td>130CS21008	</td><td>AMULYA</td><td>	2</td><td>	13</td><td>	27</td><td>	25</td><td>	17</td>	<td>26</td><td>	320</td><td>	FAIL</td></tr>
	<tr><td>130CS21009</td><td>	ANUSHA S</td><td>	2</td><td>	34</td><td>	39</td><td>	37</td><td>	29</td><td>	37</td><td>	420</td><td>	Distinction</td></tr>
	<tr><td>130CS21010	</td><td>ARCHANA R</td><td>	2</td><td>	8</td><td>	32</td><td>	28</td>	<td>16</td>	<td>20</td>	<td>274</td>	<td>FAIL</td></tr>
	<tr><td>	130CS21012</td><td>	CHANDRASHEKHAR S</td><td>	2</td><td>	24</td><td>	38</td><td>	34</td><td>	30</td><td>	34</td><td>	410</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21014</td><td>	DARSHAN K P</td><td>	2</td><td>	7</td><td>	28</td><td>	30</td><td>	8</td><td>	20</td><td>	272</td><td>	FAIL</td></tr>
<tr><td>	130CS21015</td><td>	DHANUSH M</td><td>	2</td><td>	25</td><td>	37</td><td>	37</td><td>	32</td><td>	35</td><td>	413</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21017</td><td>	DISHA N K</td><td>	2</td><td>	9</td><td>	33</td><td>	32</td><td>	10</td><td>	20</td><td>	284</td><td>	FAIL</td></tr>
<tr><td>	130CS21018</td><td>	GOWTHAM S</td><td>	2</td><td>	21</td><td>	34</td><td>	34</td><td>	34</td><td>	31</td><td>	361</td><td>	FRISTCLASS</td></tr>
<tr><td>130CS21019</td><td>	JEEVITHA M	</td><td>  2</td><td>	 5</td><td>	19</td<td>	32</td><td>	10</td><td>	20</td></td><td>	233</td><td>	FAIL</td></tr>
<tr><td>130CS21020</td><td>	JNANASHREE R </td><td>2	</td><td>14</td><td>	29</td><td>	38</td><td>	32</td><td>	34</td><td>	376</td><td>	FAIL</td></tr>
<tr><td>130CS21021</td><td>	LAKSHMI S	 </td><td> 2</td><td>14</td><td>	27</td><td>	34</td><td>	26</td><td>	30</td><td>	353</td><td>	FAIL</td></tr>
<tr><td>130CS21022</td><td>	MAHADEVAPRASAD	 </td><td>2</td><td>	25</td><td>	35</td><td>	32</td><td>	28</td><td>	31</td><td>	369</td><td>	FRISTCLASS</td></tr>
<tr><td>130CS21011</td><td>CHAITHANYAKUMARI N</td><td>2</td><td>	20</td><td>	38</td><td>	36</td><td>	24</td><td>	34</td><td>	396</td><td>	DISTINCTION</td></tr>
<tr><td>130CS21023</td><td>	MAHADEVASWAMY N	 </td><td>2</td><td>	12</td><td>	26</td><td>	27</td><td>	31</td><td>	24</td><td>	337</td><td>	FAIL</td></tr>
<tr><td>130CS21024</td><td>	MAHATHEJASWI H N </td><td>2</td><td>	41</td><td>	36</td><td>	36</td><td>	30</td><td>	33</td><td>	413</td><td>	DISTINCTION</td></tr>
<tr><td>130CS21025</td><td>	MAHENDRA U	</td><td>2</td><td>	24</td><td>25</td><td>	25</td><td>	31</td><td>	27</td><td>	323</td><td>	FRISTCLASS</td></tr>
<tr><td>130CS21026</td><td>	MALLESH M	</td><td>2</td><td>	5</td><td>23</td><td>	27</td><td>	20</td><td>	20</td><td>	273</td><td>	FAIL</td></tr>
<tr><td>130CS21029</td><td>	NAGARJUN P	</td><td>2</td><td>	5</td><td>26</td><td>	26</td><td>	20</td><td>	20</td><td>	285</td><td>	FAIL</td></tr>
<tr><td>130CS21030</td><td>NANDAKUMARA M</td><td>2</td><td>	23</td><td>32</td><td>	30</td><td>	30</td><td>	33</td><td>	374</td><td>	DISTINCTION</td></tr>
<tr><td>130CS21031</td><td>	NAVEENA R	</td><td>2</td><td>	1</td><td>18</td><td>	22</td><td>	2	</td><td>20	</td><td>214	</td><td>FAIL</td></tr>
<tr><td>	130CS21032</td><td>	NIKHIL D	</td><td>2</td><td>	38</td><td>	37</td><td>	34</td><td>	37</td><td>	37	</td><td>433</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21034</td><td>	NISARGA C	</td><td>2</td><td>	32</td><td>	36</td><td>	27</td><td>	30</td><td>	30	</td><td>388</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21035</td><td>	NISARGA K	</td><td>2</td><td>	20</td><td>	24</td><td>	24</td><td>	17</td><td>	30	</td><td>331</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21036</td><td>NITHINKUMAR R</td><td>2</td><td>	34</td><td>	27</td><td>	36</td><td>	23</td><td>	20	</td><td>328</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21037</td><td>	PRANAV P	</td><td>2</td><td>	14</td><td>	10</td><td>	32</td><td>	17</td><td>	20	</td><td>237</td><td>	FAIL</td></tr>
<tr><td>	130CS21038</td><td>	RAJEEVA	    </td><td>2</td><td>	38</td><td>	37</td><td>	34</td><td>	32</td><td>	34	</td><td>431</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21039</td><td>	RAJESHWARI S</td><td>2</td><td>	1	</td><td>24	</td><td>23	</td><td>17	</td><td>20	</td><td>262</td><td>	FAIL</td></tr>
<tr><td>	130CS21042</td><td>	ROHITH S	</td><td>2</td><td>	1	</td><td>10	</td><td>21	</td><td>8	</td><td>20	</td><td>209</td><td>	FAIL</td></tr>
<tr><td>	130CS21043</td><td>S RAGHAVENDRA</td><td>2</td><td>	32</td><td>	32</td><td>	33</td><td>	30</td><td>	37	</td><td>412</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21044</td><td>	SAHANA R	</td><td>2</td><td>	7	</td><td>26	</td><td>28	</td><td>24	</td><td>20	</td><td>288</td><td>	FAIL</td></tr>
<tr><td>	130CS21045</td><td>	SAMUEL P	</td><td>2</td><td>	44</td><td>	34</td><td>	36</td><td>	33</td><td>	37	</td><td>433</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21046</td><td>	SANDESHA N	</td><td>2</td><td>	12</td><td>	18</td><td>	21</td><td>	17</td><td>	29	</td><td>254</td><td>	FAIL</td></tr>
<tr><td>	130CS21047</td><td>	SHIVANANDA SWAMY</td><td>	2</td><td>	20</td><td>	22</td><td>	19</td><td>	18</td><td>	20</td><td>	263</td><td>	PASS</td></tr>
<tr><td>	130CS21049</td><td>	SHIVU K S	</td><td>2</td><td>	20</td><td>	26</td><td>	35</td><td>	22</td><td>	30</td><td>	338</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21050</td><td>	SOWJANYA M	</td><td>2</td><td>	20</td><td>	24</td><td>	30</td><td>	26</td><td>	24</td><td>	368</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21051</td><td>	SPANDANA S	</td><td>2</td><td>	33</td><td>	35</td><td>	32</td><td>	32</td><td>	30</td><td>	400</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21052</td><td>	SUCHITHRA K	</td><td>2</td><td>	20</td><td>	28</td><td>	30</td><td>	33</td><td>	22</td><td>	338</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21053</td><td>	SUPRIYA S JOSHI	</td><td>2</td><td>	46</td><td>	40</td><td>	38</td><td>	31</td><td>	37</td><td>	450</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21054</td><td>	SUSHMITHA K	    </td><td>2</td><td>	25</td><td>	33</td><td>	35</td><td>	20</td><td>	38</td><td>	339</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21055</td><td>	SYED UMAR FAROOQ</td><td>2</td><td>	5	</td><td>18	</td><td>31	</td><td>6</td><td>	20</td><td>	242</td><td>	FAIL</td></tr>
<tr><td>	130CS21056</td><td>	SYEDA MALEEHA	</td><td>2</td><td>	29</td><td>	30</td><td>	34</td><td>	17</td><td>	35</td><td>	384</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21057</td><td>	T R KEERTHANA	</td><td>2</td><td>	23</td><td>	22</td><td>	33</td><td>	26</td><td>	32</td><td>	365</td><td>	FRISTCLASS</td></tr>
<tr><td>	130CS21058</td><td>	THARUN S	    </td><td>2</td><td>	10</td><td>	16</td><td>	36</td><td>	24</td><td>	22</td><td>	266</td><td>	FAIL</td></tr>
<tr><td>	130CS21059</td><td>	UDAY T	        </td><td>2</td><td>	20</td><td>	28</td><td>	31</td><td>	30</td><td>	37</td><td>	370</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21060</td><td>	VARSHINI Y M	</td><td>2</td><td>	26</td><td>	26</td><td>	35</td><td>	30</td><td>	35</td><td>	401</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21061</td><td>	VARUN M	        </td><td>2</td><td>	34</td><td>	20</td><td>	31</td><td>	27</td><td>	24</td><td>	318</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21062</td><td>	VIGNESH D	    </td><td>2</td><td>	31</td><td>	40</td><td>	37</td><td>	35</td><td>	37</td><td>	436</td><td>	DISTINCTION</td></tr>
<tr><td>	130CS21063</td><td>	VINAY G	        </td><td>2</td><td>	29</td><td>	34</td><td>	36</td><td>	34</td><td>	37</td><td>	419</td><td>	DISTINCTION</td></tr>
    </table>"""
   st.markdown(table,unsafe_allow_html=True)
st.container()
