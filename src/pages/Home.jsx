import { useTranslation } from 'react-i18next';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Home = () => {
  const { t } = useTranslation();

  return (
    <>
      <Navbar />

      <section id="intro">
        <h1>{t('home.title')}</h1>
        <p>{t('home.subtitle')}</p>
        <div className="project-links">
          <a href="https://uzcoin.uzinex.uz">{t('home.projects.uzcoin')}</a>
          <a href="https://freelance.uzinex.uz">{t('home.projects.freelance')}</a>
          <a href="https://host.uzinex.uz">{t('home.projects.host')}</a>
          <a href="https://bank.uzinex.uz">{t('home.projects.bank')}</a>
        </div>
      </section>

      <section id="contact">
        <h2>{t('navbar.contact')}</h2>
        <p><a href="https://t.me/uzinex">{t('contact.telegram')}</a></p>
        <p><a href="https://threads.net/@uzinex_official">{t('contact.threads')}</a></p>
        <p>{t('contact.email')}: info@uzinex.uz</p>
      </section>

      <Footer />
    </>
  );
};

export default Home;
